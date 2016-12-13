class Bunch(dict):
    """Container object for datasets
    Dictionary-like object that exposes its keys as attributes.
    >>> b = Bunch(a=1, b=2)
    >>> b['b']
    2
    >>> b.b
    2
    >>> b.a = 3
    >>> b['a']
    3
    >>> b.c = 6
    >>> b['c']
    6
    """

    def __init__(self, **kwargs):
        super(Bunch, self).__init__(kwargs)

    def __setattr__(self, key, value):
        self[key] = value

    def __dir__(self):
        return self.keys()

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key)


def save_object(obj, filename):
	import pickle as pickle
	with open(filename, 'wb') as output:
		pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)


if __name__=="__main__":
		X = [(1,2),(2,3),(3,4)]
		Y = [1,2,3]

		dataset = Bunch(data=X, target=Y)
		import pickle as pickle
		save_object(dataset,'data.pkl')

		with open('data.pkl', "rb") as f:
				data = pickle.load(f)
				X = data.data
				Y = data.target
		print(X)
		print(Y)
