var divCcaContent;

function GetAllElementsWithAttribute(ParentElement, Attribute)
{
  if (typeof ParentElement === 'undefined' || ParentElement === null) 
  {
    return null;
  }
  var MatchingElements = [];
  var AllElements = ParentElement.getElementsByTagName('*');
  for (var i = 0, n = AllElements.length; i < n; i++)
  {
    if (AllElements[i].getAttribute(Attribute) !== null)
    {
      // Element exists with attribute. Add to array.
      MatchingElements.push(AllElements[i]);
    }
  }
  return MatchingElements;
}

function GetElementByUniqueId(ParentElement, UniqueId)
{
  var Elements = GetAllElementsWithAttribute(ParentElement, 'uniqueidentifier');
  if(Elements != null)
  {
    for(var i = 0; i < Elements.length; i++)
    {
      if(Elements[i].getAttribute('uniqueidentifier') == UniqueId)
      {
        return Elements[i];
      }
    }
  }
  return null;
}

function GetCcaElementByUniqueId(UniqueId)
{
  if (typeof divCcaContent == 'undefined' || divCcaContent == null) 
  {
    AllDivs = document.getElementsByTagName('div');
    for (var i = 0; i < AllDivs.length; i++)
    {
      if(AllDivs[i].id.indexOf('ccaContent') != -1)
      {
        divCcaContent = AllDivs[i];
        break;
      }
    }
  }
  return GetElementByUniqueId(divCcaContent, UniqueId);
}