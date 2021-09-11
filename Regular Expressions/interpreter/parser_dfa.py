# utf-8

class RegExp(object):

    SPLIT = 256
    MATCH = 257

    def __init__(self) -> None:
        '''
        state_num: 为 nfa 中的每一个状态赋予唯一 id
        list_id: 标识当前处于的 NFA 片段列表，在匹配过程中，每匹配一个字符，
        会新建一个列表，同时使 list_id 递增1
        dstate: DFA 中的所有状态，构造为二叉搜索树
        '''
        self.state_num = 0
        self.list_id = 0
        self.dstate = None

    def get_state_num(self):
        '''
        该函数用于为 非确定有限状态自动机(NFA) 中的每个状态分配一个唯一的 id
        '''
        self.state_num += 1
        return self.state_num

    def post2nfa(self, postfix):
        '''
        postfix: 正则表达式后缀表达式
        该函数用于将正则表达式后缀表达式解析为 NFA
        '''
        # operand
        frags = []

        for item in postfix:
            if item == '.':  # ! catenate，本解析器将.作为显示连接符
                e2 = frags.pop()
                e1 = frags.pop()
                self.patch(e1.out, e2.start)
                frags.append(RegExp.Frag(e1.start, e2.out))
            elif item == '|':  # ! alternate
                e2 = frags.pop()
                e1 = frags.pop()
                s = RegExp.State(self.get_state_num(), RegExp.SPLIT)
                s.out = e1.start
                s.out1 = e2.start
                frags.append(RegExp.Frag(s, self.append(e1.out, e2.out)))
            elif item == '?':  # ! zero or one
                e = frags.pop()
                s = RegExp.State(self.get_state_num(), RegExp.SPLIT)
                s.out = e.start
                frags.append(RegExp.Frag(
                    s, self.append(e.out, self.list1((s, 'out1')))))
            elif item == '*':  # ! zero or more
                e = frags.pop()
                s = RegExp.State(self.get_state_num(), RegExp.SPLIT)
                s.out = e.start
                self.patch(e.out, s)
                frags.append(RegExp.Frag(s, self.list1((s, 'out1'))))
            elif item == '+':  # ! one or more
                e = frags.pop()
                s = RegExp.State(self.get_state_num(), RegExp.SPLIT)
                s.out = e.start
                self.patch(e.out, s)
                frags.append(RegExp.Frag(e.start, self.list1((s, 'out1'))))
            else:
                s = RegExp.State(self.get_state_num(), item)
                frags.append(RegExp.Frag(s, self.list1((s, 'out'))))

        e = frags.pop()

        #! 此时 frags 应为空，否则正则表达式不合法
        if frags:
            return False

        #! e.out 表示 NFA 的所有出口，若输入字符串可到达出口，认为 NFA 能够匹配该字符串
        self.patch(e.out, RegExp.State(self.get_state_num(), RegExp.MATCH))
        return e.start

    def re2post(self, regex):
        '''
        regex: 正则表达式
        该函数用于将输入的中缀正则表达式解析为后缀表达式
        '''
        # * nalt 表示 | 的个数
        nalt = 0
        # * natom 表示 目前操作数的个数
        natom = 0
        # * paren 存储括号外部的 nalt 和 natom 的个数，每当遇到一个 (，就添加一个元组 (nalt, natom)
        paren = []
        res = ""
        for c in regex:
            if c == '(':
                if natom > 1:
                    natom -= 1
                    res += '.'
                paren.append((nalt, natom))
                nalt = 0
                natom = 0
            elif c == '|':
                if natom == 0:
                    return False
                while natom > 1:
                    natom -= 1
                    res += '.'
                natom = 0
                nalt += 1
            elif c == ')':
                if not paren:
                    return False
                if natom == 0:
                    return False
                while natom > 1:
                    natom -= 1
                    res += '.'

                while nalt > 0:
                    nalt -= 1
                    res += '|'

                nalt, natom = paren.pop()
                natom += 1
            elif c == '*' or c == '+' or c == '?':
                if natom == 0:
                    return False

                res += c
            else:
                if natom > 1:
                    natom -= 1
                    res += '.'
                res += c
                natom += 1

        if paren:
            return False

        while natom > 1:
            natom -= 1
            res += '.'
        while nalt > 0:
            nalt -= 1
            res += '|'

        return res

    def list1(self, item):
        '''
        item: (state, outtype)
        其中outtype可取 'out'和'out1'
        分别表示状态state的out指针和out1指针
        '''
        return [item]

    def patch(self, out, state):
        '''
        out: NFA 片段的所有出口
        state: 某状态 s
        该函数用于将 该片段的所有出口与 state 连接
        '''
        for item, out_type in out:
            if out_type == 'out':
                item.out = state
            else:
                item.out1 = state

    def append(self, out1, out2):
        '''
        out1: NFA 片段1出口
        out2: NFA 片段2出口
        该函数用于将片段1出口和片段2出口合并
        '''
        return out1+out2

    def step(self, cstates, c, nstates):
        '''
        cstates: 目前所有成功匹配的 NFA 片段
        c: 待匹配的字符
        nstates: 下一状态列表，用于存储所有成功匹配 c 的 NFA 片段
        该函数用于在目前所有成功匹配的 NFA 片段中匹配字符 c，若成功匹配，
        则将该 NFA 片段的下一状态加入 nstates 列表，用于匹配下一字符
        '''
        self.list_id += 1
        for state in cstates:
            if state.c == c:
                self.add_state(nstates, state.out)

    def add_state(self, states, state):
        '''
        states: NFA 片段列表
        state: 待添加的 state/nfa
        该函数用于将 state 添加至 states，注意
        1. 空状态/已存在的状态不能重复添加
        2. SPLIT 状态时，应添加其两个分支状态
        '''
        # state 为空 或 state 已经在 states 中，不重复添加
        if state is None or state.lastlist == self.list_id:
            return

        state.lastlist = self.list_id
        if state.c == RegExp.SPLIT:
            # 添加两个分支状态
            self.add_state(states, state.out)
            self.add_state(states, state.out1)
            return
        states.append(state)

    def start_states(self, states, start):
        '''
        states: NFA 片段列表
        start: NFA
        该函数用于使初始化 NFA 片段列表
        '''
        self.list_id += 1
        self.add_state(states, start)
        return states

    class Frag(object):
        def __init__(self, start, out=None) -> None:
            '''
            start: 表示 NFA 片段中的开始状态
            out: 表示 NFA 片段中的所有仍未连接的 state，由于python为按值传递，因此，传递元组(out, outtype)，使用out.outtype进行连接
            (s, 'out')表示s.out
            (s, 'out1')表示s.out1
            在 NFA 生成的最后，应使这些未连接的连接至 MATCH state
            Frag 类用于简化 NFA 的生成，通过缓存 NFA 片段的所有 out，而不是每次遍历 state 列表获取未连接的 state，可以大大加快运行速度
            '''
            # start state
            self.start = start
            # * list of out state item: (out, outtype)
            # * eg: (s, 'out') -> s.out
            # * (s, 'out1') -> s.out1
            self.out = out

    class State(object):
        def __init__(self, id, c) -> None:
            '''
            id: 表示 state 唯一 id
            c: state 表示的字符，c<256时，表示待匹配的字符，c=256时，表示 SPLIT 状态，c=257时，表示 MATCH 状态
            out: state 连接的下一个状态
            out1: 仅在 c 为 SPLIT状态 时使用，此时 out 和 out1 用于连接两种不同的选择（状态）
            lastlist: 用于标识 state 所处的 state 列表，在运行时用于防止重复添加
            State 事实上就是 NFA(片段)，就像树节点就是树，只不过 c<=256 时，out/out1 并不连接 MATCH 状态，而是存在一或多条无连接的出口，指向None
            '''
            self.id = id
            self.c = c
            self.out = None
            self.out1 = None
            self.lastlist = 0

    class DState(object):
        def __init__(self, states) -> None:
            '''
            states: DFA 中的一个状态相当于 NFA 中的状态（片段）集
            next: 保存所有指向下一状态的指针，大小为256（扩展后的ascii码），
            若当前状态为 d，输入字符为 c，那么 d.next[c] 即为下一状态，若 d.next[c] 为 None，说明还未连接
            left: 树左分支
            right: 树右分支
            '''
            self.states = states
            self.next = [None for _ in range(256)]
            self.right = None
            self.left = None

    def match(self, start, input_str):
        '''
        start: DFA
        input_str: 输入字符串
        该函数用于使用 DFA 匹配输入的字符串
        '''
        for c in input_str:
            index = ord(c)
            if start.next[index]:
                next_state = start.next[index]
            else:
                next_state = self.next_dstate(start, c)
            start = next_state
        return self.is_match(start.states)

    def is_match(self, states):
        '''
        states: 遍历输入字符串之后所有成功匹配的 NFA 片段
        该函数用于检验遍历完毕后，剩余合法的 NFA 片段中是否处于MATCH状态，
        若某 NFA 片段处于 MATCH 状态，则成功匹配
        '''
        for state in states:
            if state.c == RegExp.MATCH:
                return True

        return False

    def states_cmp(self, states1, states2):
        '''
        states1: NFA 片段的状态集
        states2: NFA 片段的状态集
        该函数用于比较 DFA 的两个状态，规则为:
        1. 若 len(states1) < len(states2)，返回 -1
        2. 若 len(states1) > len(states2)，返回 1
        3. 若二者长度一样，则比较 states1 和 states2 中的每一个 state 的内存地址
        '''
        if len(states1) < len(states2):
            return -1
        if len(states1) > len(states2):
            return 1

        for i in range(len(states1)):
            if id(states1[i]) < id(states2[i]):
                return -1
            elif id(states1[i]) > id(states2[i]):
                return 1
        return 0

    def get_dstate(self, states):
        '''
        states: 状态集
        该函数以状态集作为 key，获取该状态集对应的 DState
        '''
        # 排序
        states.sort(key=lambda state: id(state))

        # 循环目前的 dstate
        dstate = self.dstate
        while dstate:
            cmp = self.states_cmp(states, dstate.states)
            if cmp < 0:
                dstate = dstate.left
            elif cmp > 0:
                dstate = dstate.right
            else:
                return dstate

        # 新建dstate
        dstate = RegExp.DState(states)
        return dstate

    def start_dstate(self, start):
        '''
        start: state(也就是NFA)
        该函数根据 NFA 获取初始 DFA
        '''
        states = []
        return self.get_dstate(self.start_states(states, start))

    def next_dstate(self, dstate, c):
        '''
        dstate: DFA 片段
        c: 输入字符
        该函数根据当前 DFA 和输入字符获取 DFA 的下个状态（也即 NFA 的状态集）
        '''
        nstates = []
        self.step(dstate.states, c, nstates)
        dstate.next[ord(c)] = self.get_dstate(nstates)
        return dstate.next[ord(c)]


def main():
    regex = RegExp()
    post = regex.re2post(r'a(b*|c)*a')
    print(post)
    if not post:
        print("正则表达式语法错误：{}".format(regex))
    start = regex.post2nfa(post)
    input_str = ['aa', 'acccca', 'abbbbba']
    for item in input_str:
        if(regex.match(regex.start_dstate(start), item)):
            print(item)


main()
