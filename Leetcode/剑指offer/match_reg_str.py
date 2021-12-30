class Solution:

    SPLIT = 256
    MATCH = 257

    def __init__(self) -> None:
        '''
        state_num: 为 nfa 中的每一个状态赋予唯一 id
        list_id: 标识当前处于的 NFA 片段列表，在匹配过程中，每匹配一个字符，
        会新建一个列表，同时使 list_id 递增1
        '''
        self.state_num = 0
        self.list_id = 0

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
            if item == '#':  # ! catenate，本解析器将 # 作为显式连接符
                e2 = frags.pop()
                e1 = frags.pop()
                self.patch(e1.out, e2.start)
                frags.append(Solution.Frag(e1.start, e2.out))
            elif item == '*':  # ! zero or more
                e = frags.pop()
                s = Solution.State(self.get_state_num(), Solution.SPLIT)
                s.out = e.start
                self.patch(e.out, s)
                frags.append(Solution.Frag(s, self.singletonlist((s, 'out1'))))
            else:
                s = Solution.State(self.get_state_num(), item)
                frags.append(Solution.Frag(s, self.singletonlist((s, 'out'))))

        e = frags.pop()

        #! 此时 frags 应为空，否则正则表达式不合法
        if frags:
            return False

        #! e.out 表示 NFA 的所有出口，若输入字符串可到达出口，认为 NFA 能够匹配该字符串
        self.patch(e.out, Solution.State(self.get_state_num(), Solution.MATCH))
        return e.start

    def re2post(self, regex):
        '''
        regex: 正则表达式
        该函数用于将输入的中缀正则表达式解析为后缀表达式
        '''
        # * natom 表示 目前操作数的个数
        natom = 0
        res = ""
        for c in regex:
            if c == '*':
                if natom == 0:
                    return False

                res += c
            else:
                if natom > 1:
                    natom -= 1
                    res += '#'
                res += c
                natom += 1

        while natom > 1:
            natom -= 1
            res += '#'

        return res

    def singletonlist(self, item):
        '''
        item: (state, outtype)
        其中outtype可取 'out'和'out1'
        分别表示状态state的out指针和out1指针
        '''
        return [item]

    def patch(self, out, state):
        '''
        out: NFA 片段的所有未连接的指针
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
        out1: NFA 片段1所有未连接的指针
        out2: NFA 片段2所有未连接的指针
        该函数用于将片段1的未连接的指针和片段2的未连接的指针合并
        '''
        return out1+out2

    def match(self, start, input_str):
        '''
        start: NFA
        input_str: 待匹配字符串
        该函数使用构建成功的 NFA 匹配输入的字符串，若成功匹配则返回True
        '''
        cstates = []  # ! current states
        nstates = []  # ! next states

        # 根据 NFA 构建初始状态集
        cstates = self.start_states(cstates, start)

        for c in input_str:
            self.step(cstates, c, nstates)
            cstates = nstates
            nstates = []

        return self.is_match(cstates)

    def is_match(self, states):
        '''
        states: 遍历输入字符串之后所有成功匹配的 NFA 片段
        该函数用于检验遍历完毕后，剩余合法的 NFA 片段中是否处于MATCH状态，
        若某 NFA 片段处于 MATCH 状态，则成功匹配
        '''
        for state in states:
            if state.c == Solution.MATCH:
                return True

        return False

    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        post = self.re2post(p)

        start = self.post2nfa(post)
        return self.match(start, s)

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
            if state.c == c or state.c == '.':
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
        if state.c == Solution.SPLIT:
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


def main():
    regex = Solution()
    post = regex.re2post(r'')
    print(post)
    if not post:
        print("正则表达式语法错误：{}".format(regex))
    start = regex.post2nfa(post)
    input_str = ['aa', 'acccca', 'abbbbba']
    for item in input_str:
        if(regex.match(start, item)):
            print(item)


main()
