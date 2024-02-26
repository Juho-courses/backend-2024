class Base:
    def save(self, data):
        self.data = data


class Model(Base):
    data: int

    def print(self):
        print(self.data)


b = Base()
b.save("kissa")
print(b.data)

m = Model()
m.save(123)
m.print()
