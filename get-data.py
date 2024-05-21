from ucimlrepo import fetch_ucirepo 
import os
  
def get_data(id, name, dirname):
    filename = os.path.join(dirname, f'data/{name}.csv')
    df = fetch_ucirepo(id=id)
    df.data.original.to_csv(filename, index=False)

if __name__ == '__main__':
    dirname = os.path.dirname(__file__)
    get_data(1, 'abalone', dirname)