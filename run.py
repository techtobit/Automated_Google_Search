from Google_Search import GSearch

action = GSearch.Search()
keyword = 'Ridme 10'
action.gSarch(keyword)
result = action.getResult()
action.saveResult(result)
action.closeBrowser()