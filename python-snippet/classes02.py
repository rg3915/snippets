class X(object):

    def run(self):
        try:
            self._do_run()
        except Exception as e:
            raise e.treat_error()

    def _do_run(self):
        print("aaaa")


class Y(X):

    def _do_run(self):
        print("bbbbb")
