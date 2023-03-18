class BrowserHistory:

    def __init__(self, homepage: str):
        self.URLsHistory = [homepage]
        self.currURL = 0
        self.lastURL = 0
    
    def visit(self, url: str) -> None:
        self.currURL += 1
        if len(self.URLsHistory) > self.currURL:
            self.URLsHistory[self.currURL] = url
        else:
            self.URLsHistory.append(url)
        self.lastURL = self.currURL
    
    def back(self, steps: int) -> str:
        self.currURL = max(0, self.currURL - steps)
        return self.URLsHistory[self.currURL]
    
    def forward(self, steps: int) -> str:
        self.currURL = min(self.lastURL, self.currURL + steps)
        return self.URLsHistory[self.currURL]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)