class Node(object):
    def __init__(self, choice,left=None, middle=None, right=None):
        self.left = left
        self.middle = middle
        self.right = right
        self.body = choice

    def set(self,left=None, middle=None, right=None):
        self.left = left
        self.middle = middle
        self.right = right

    def route(self):
        current = self
        while (True):
            if (current.left==None and current.right==None):
                print(current.body)
                print("test over")
                break;
            else:
                print(current.body)
                choice = input("1, 2 or 3:")
                if (choice=='1'):
                    current = current.left
                elif choice == '2':
                    current = current.right
                elif choice == '3':
                    current = current.middle
                else:
                    print("wrong input")

root = Node("你知道什么是丧吗\nyes/no/depends")
q2 = Node("你在生活中，积极在态度比消极的态度多吗 \nyes/no/depends")
q3 = Node("你会去嘲笑别人的丧吗\nyes/no/depends")
q4 = Node('你觉得不努力的人能够过上好的生活吗\nyes/no/depends')
q5 = Node('你身边不努力的人有很多吗\nyes/no/depends')
q6 = Node('你的情绪会影响到别人的心情吗\nyes/no/depends')
q7 = Node('你喜欢去影响别人的心情吗\nyes/no/depends')
q8 = Node('你能够好好的过自己的生活吗\nyes/no/depends')
q9 = Node('你觉得沮丧的情绪好对付吗\nyes/no/depends')
q10 = Node('你的情绪是谁给你的\nyourself/job/depends')
a1 = Node('你的丧属于最高等级 \n你的丧已经达到了最高级了，你全身上下都是满满的负能量，一靠近你就会感觉到一股不安的气息。你并不想去努力的生活，你也不想有所发展，你觉得得过且过生活并没有什么不好的，碌碌无为的生活你也很满足，即使别人看不起你，你也无动于衷。')
a2 = Node('你的丧属于中级 \n你的丧属于中级，一不注意你就会变成一个很丧的人了，你自己应该要多加注意一些才是。你很容易被身边的人影响，因此你经常处在举棋不定的状态中，你心里有两个声音，一个是天使，一个是魔鬼。你并不是每一次都能够很好的控制住自己的情绪的。')
a3 = Node('你的丧属于最低等级 \n你并不是很丧，偶尔丧你是有的，你自己也能够接受自己偶尔丧的状态，但是你很快就调整好自己的心态。在你看来，生活不管是开心还是不开心都是一天一天的过，你觉得不开心的过还不如开开心心的过。你不希望自己被不好的情绪牵着走的，你还是很努力的。')
a4 = Node('你的丧排不上级别 \n你是一个心态特别好的人，丧这种状态在你的生活中是不会出现的，你不允许自己有这样的状态，你是一个很积极的人。不管生活是什么样子的，你都不会妥协和害怕，你的发展会越来越好，前途一片光明，你总是给身边的人带来一些正能量，没有任何的不好情绪出现。')
root.set(q2, q4, q3)
q2.set(q4, q3, q6)
q3.set(q4,q7,q5)
q4.set(q6,q7,q8)
q5.set(q7,q8,q6)
q6.set(q9,q7,q10)
q7.set(q8,q10,q9)
q8.set(q9,a3,q10)
q9.set(a4,a2,q10)
q10.set(a1,a2,a3)

while True:
    root.route()
