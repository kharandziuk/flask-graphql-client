from graphqlclient import GraphQLClient
import ssl

# HACK: dirty to overcome certificate problems. DON'T USE IN PRODUCITON
ssl._create_default_https_context = ssl._create_unverified_context

URL = 'https://web-backend-dev.zeitgold.com/graphql'

client = GraphQLClient(URL)

result = client.execute('''
{
    business(id:"QnVzaW5lc3NOb2RlOjE0Mjc2Y2FhLTA4NmEtNGVmNi04NzMxLTNmYWUzMjE3ZjVlZQ==") {
         name
    }
}
''')

print(result)
