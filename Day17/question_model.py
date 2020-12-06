class Question:
    def __init__(self,text="",ans=True):
        self.text = text
        self.ans=ans

    def __str__(self):
        return f"{self.text}  -  {self.ans}"