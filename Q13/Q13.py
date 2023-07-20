class Rev:
    @staticmethod
    def rev(word):
        return " ".join(word.split(" ")[::-1])
 
print(Rev.rev("hello Python"))