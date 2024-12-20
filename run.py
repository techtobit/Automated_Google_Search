from Google_Search import GSearch

# keyword = input('Write the keyword : ')
keyword = 'GEEPAS'
action = GSearch.Search(keyword)
action.gSarch()
result = action.getResult()
action.saveResult(result)
action.closeBrowser()