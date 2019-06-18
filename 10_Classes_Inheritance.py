class SortedList(list):
  def append(self,value):
    self.sort()
    super().append(value)
    self.sort()