from app.models import Caption

#-----------------------------------------------------------------------
# GetCaptions - returns the captions for an application ID and language
#-----------------------------------------------------------------------

def T_GetCaptions(appid, langid):
  
  captionSet = Caption.objects.filter(app=appid, lang=langid)
    
  captions = {}
  
  for x in captionSet:
    # we need to repalce hyphens to undderscore to prevent parse errors in template
    captions["K_" + x.id.replace("-", "_")] = {"caption": x.caption}
 
  return captions

#-----------------------------------------------------------------------
# GetCationById - returns the caption for an application ID,
#                 language and caption ID
#-----------------------------------------------------------------------

def T_GetCationById(appid, langid, captionID):
  
  caption = Caption.objects.filter(id=captionID, app=appid, lang=langid)
    
  captions = {}
  captions["langID"] = langid
  captions["appID"] = appid
  captions["capationID"] = captionID
  captions["msg"] = caption.caption
 
  return captions

