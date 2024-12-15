from Google_Search import GSearch

action = GSearch.Search()
action.gSarch('VS CODE')
result = action.getResult()
action.saveResult(result)
action.closeBrowser()