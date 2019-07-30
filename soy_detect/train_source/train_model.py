
import chainer
import chainer.links as L
import chainer.functions as F
from chainer import Link, Chain, ChainList



class MyChain(Chain):
	def __init__(self):
		super(MyChain, self).__init__(
			cn1 = L.Convolution2D(None, 16, 5, pad=2),
			cn2 = L.Convolution2D(None, 32, 5,pad=2),
			l1 = L.Linear(None, 500),
			l2 = L.Linear(None, 4),		#出力層は識別するクラス数
		)

	def __call__(self, x, t):
		return F.softmax_cross_entropy(self.fwd(x), t)

	def fwd(self, x):

		h1 = F.max_pooling_2d(F.relu(self.cn1(x)), 2)
		h2 = F.max_pooling_2d(F.relu(self.cn2(h1)), 2)
		h3 = F.dropout(F.relu(self.l1(h2)))
		return self.l2(h3)
