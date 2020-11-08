# https://www.codewars.com/kata/515bb423de843ea99400000a/train/python

# TODO: complete this class

class PaginationHelper:

  # The constructor takes in an array of items and a integer indicating
  # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection # array of values
        self.items_per_page = items_per_page
  
  # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)
  
  # returns the number of pages
    def page_count(self):
        self.quotient, self.remainder = divmod(self.item_count(), self.items_per_page)
        return self.quotient + (0 if not self.remainder else 1) # if there's a remainder add a page
	
  # returns the number of items on the current page. page_index is zero based
  # this method should return -1 for page_index values that are out of range
    def page_item_count(self,page_index):
        if page_index > self.page_count() - 1 or page_index < 0: return -1
        if not self.remainder: 
            return self.items_per_page
        else:
            if page_index == self.page_count() - 1: 
                return self.remainder
            else: 
                return self.items_per_page

  # determines what page an item is on. Zero based indexes.
  # this method should return -1 for item_index values that are out of range
    def page_index(self,item_index):
        if item_index > self.item_count() - 1 or item_index < 0: return -1
        if item_index < self.items_per_page: 
            return 0 # if less than total items on a page return 1st page
        else:
            a, b = divmod(item_index, self.items_per_page)
            return (a + (0 if not b else 1)) - 1 #zero index
      
  



#tests
helper = PaginationHelper(['a','b','c','d','e','f'], 4)
print(helper.item_count()) # should == 6
print(helper.page_count()) # should == 2
print(helper.page_item_count(0))  # should == 4
print(helper.page_item_count(1)) # last page - should == 2
print(helper.page_item_count(2)) # should == -1 since the page is invalid
print(helper.page_index(5)) # should == 1 (zero based index)
print(helper.page_index(2)) # should == 0
print(helper.page_index(20)) # should == -1
print(helper.page_index(-10)) # should == -1 because negative indexes are invalid




"""
CodeWars best practice version:


class PaginationHelper:

  # The constructor takes in an array of items and a integer indicating
  # how many items fit within a single page
  def __init__(self, collection, items_per_page):
    self.collection = collection
    self.items_per_page = items_per_page
      
  
  # returns the number of items within the entire collection
  def item_count(self):
    return len(self.collection)
  
  # returns the number of pages
  def page_count(self):
    if len(self.collection) % self.items_per_page == 0:
      return len(self.collection) / self.items_per_page
    else:
      return len(self.collection) / self.items_per_page + 1
    
      
    
  # returns the number of items on the current page. page_index is zero based
  # this method should return -1 for page_index values that are out of range
  def page_item_count(self,page_index):
    if page_index >= self.page_count():
      return -1
    elif page_index == self.page_count() - 1:
      return len(self.collection) % self.items_per_page or self.items_per_page
    else:
      return self.items_per_page
        
      
  
  # determines what page an item is on. Zero based indexes.
  # this method should return -1 for item_index values that are out of range
  def page_index(self,item_index):
    if item_index >= len(self.collection) or item_index < 0:
      return -1
    else:
      return item_index / self.items_per_page
"""