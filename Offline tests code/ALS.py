import numpy as np
from implicit import _als


class Als:

    def __init__(self,
                 num_factors=40,
                 regularization=0.01,
                 alpha=1.0,
                 iterations=15,
                 use_native=True,
                 num_threads=0,
                 dtype=np.float64):
        """
        Class version of alternating least squares implicit matrix factorization
        Args:
            num_factors (int): Number of factors to extract
            regularization (double): Regularization parameter to use
            iterations (int): Number of alternating least squares iterations to
            run
            use_native (bool): Whether or not to use Cython solver
            num_threads (int): Number of threads to run least squares iterations.
            0 means to use all CPU cores.
            dtype (np dtype): Datatype for numpy arrays
        """
        self.num_factors = num_factors
        self.regularization = regularization
        self.alpha = alpha
        self.iterations = iterations
        self.use_native = use_native
        self.num_threads = num_threads
        self.dtype = dtype

        self.user_vectors = None
        self.item_vectors = None
        self.solver = None

    def fit(self, Cui):
        """
        Fit an alternating least squares model on Cui data
        Args:
            Cui (sparse matrix, shape=(num_users, num_items)): Matrix of
            user-item "interactions"
        """

        users, items = Cui.shape

        self.user_vectors = np.random.normal(size=(users, self.num_factors)) \
            .astype(self.dtype)

        self.item_vectors = np.random.normal(size=(items, self.num_factors)) \
            .astype(self.dtype)

        self.solver = _als.least_squares
        self.fit_partial(Cui)

    def fit_partial(self, Cui):
        """Continue fitting model"""
        # scaling
        Cui = Cui.copy()
        Cui.data *= self.alpha
        Cui, Ciu = Cui.tocsr(), Cui.T.tocsr()

        for iteration in range(self.iterations):
            self.solver(Cui,
                        self.user_vectors,
                        self.item_vectors,
                        self.regularization,
                        self.num_threads)
            self.solver(Ciu,
                        self.item_vectors,
                        self.user_vectors,
                        self.regularization,
                        self.num_threads)

    def predict(self, user, item):
        """Predict for single user and item"""
        return self.user_vectors[user, :].dot(self.item_vectors[item, :].T)

    def predict_for_customers(self, ):
        """Recommend products for all customers"""
        return self.user_vectors.dot(self.item_vectors.T)

    def predict_for_items(self, norm=True):
        """Recommend products for all products"""
        pred = self.item_vectors.dot(self.item_vectors.T)
        if norm:
            norms = np.array([np.sqrt(np.diagonal(pred))])
            pred = pred / norms / norms.T
        return pred
