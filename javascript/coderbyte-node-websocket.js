
const onCreateMessage = ({ quantity, itemName}) => {
 return `Created ${quantity} of ${itemName}`
}

const onModifyMessage = ({itemId, action, amount}) => {
  return `Item ${itemId} quantity ${action}ed by ${amount}`
}

const onQueryMessage = ({queryType, queryValue}) => {
 return `Query of type ${queryType} with value ${queryValue} processed`
}

function advancedWebsocketHandler(messages) {

  const handlers = {
    'create': onCreateMessage,
    'modify': onModifyMessage,
    'query': onQueryMessage,
  }

  return messages.map(msg => {
    const parsedMessage = JSON.parse(msg);
    const { type, payload } = parsedMessage


    if(Object.prototype.hasOwnProperty.call(handlers, type)){
      return handlers[type](payload)
    } else {
      'Unkown message type';
    }


  })
}

console.log(
  advancedWebsocketHandler([
    '{"type":"create","payload":{"itemName":"Book","quantity":10}}',
    '{"type":"modify","payload":{"itemId":7,"action":"subtract","amount":3}}',
    '{"type":"query","payload":{"queryType":"availability","queryValue":"high"}}',
  ])
);