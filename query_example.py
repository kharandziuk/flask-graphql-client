import ssl
import json
from graphqlclient import GraphQLClient

# HACK: dirty to overcome certificate problems. DON'T USE IN PRODUCITON
ssl._create_default_https_context = ssl._create_unverified_context

URL = 'https://web-backend-dev.zeitgold.com/graphql'

client = GraphQLClient(URL)

result = client.execute('''{
    business(id: "QnVzaW5lc3NOb2RlOjE0Mjc2Y2FhLTA4NmEtNGVmNi04NzMxLTNmYWUzMjE3ZjVlZQ==") {
        businessTransactions {
          edges {
            node {
              payables {
                edges {
                  node {
                    id
                    amount
                    referenceId
                    dateOccurred
                  }
                }
              }
            }
          }
        }
    }
}''')
result = json.loads(result)
nodes = [
    payables_edges['node']
    for payable in result['data']['business']['businessTransactions']['edges']
    for payables_edges in payable['node']['payables']['edges']
]
print(nodes)
