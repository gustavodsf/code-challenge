const https = require('https');

const removeDuplicates = (array) => {
  const unique = new Set();

  for(const item of array){
    const  itemString = JSON.stringify(item);
    if(!unique.has(itemString)){
      unique.add(itemString)
    }
  }
  
  return Array.from(unique).map( item => JSON.parse(item))

}

const cleanObject = (obj) => {
  if(Array.isArray(obj)){
    return obj.map(cleanObject).filter(item => item != null && item != undefined && item != '');
  }  else if( obj != null && typeof obj == 'object'){
    const cleanned = {};
    Object.keys(obj).forEach(key => {
      const value = cleanObject(obj[key]);
      if(value != '' && value != null && value != undefined){
        cleanned[key] = value;
      }
    });
    return Object.keys(cleanned).length > 0 ? cleanned : null;
  }
  return obj;
}

const sortObjectKeys = (obj) => {
  if(Array.isArray(obj)){
    return obj.map(sortObjectKeys)
  }  else if( obj != null && typeof obj == 'object'){
    const sorted = {}
    Object
      .keys(obj)
      .sort((first, second) => first.toLowerCase().localeCompare(second.toLowerCase()))
      .forEach(key => {
        sorted[key] = sortObjectKeys(obj[key]);
      });

    return sorted;
  }
  return obj
}

https.get('https://coderbyte.com/api/challenges/json/wizard-list', (resp) => {
  
  let data = '';

  resp.on('data', chunk => data += chunk)

  resp.on('end', () =>  {
    try{
      let jsonData = JSON.parse(data);
      
      jsonData = sortObjectKeys(jsonData);
      jsonData = removeDuplicates(jsonData);
      jsonData = cleanObject(jsonData);
      
      console.log(jsonData)
    }catch(error){
      console.log('Error processing data:', error)
    }
  })
});