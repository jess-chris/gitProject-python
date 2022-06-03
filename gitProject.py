import os, sys, json

env_params = [         
        "PORT=5000 \n",
        "DB_USERNAME=aainstructor \n",
        "DB_PASSWORD=password \n",
        "DB_DATABASE=aastudent \n",
        "DB_HOST=localhost \n",
        "JWT_SECRET=U3VwZXJEdXBlclNlY3JldA== \n",
        "JWT_EXPIRES_IN=604800 \n"
        ]

package_params = {
        "start": "per-env",
        "start:development": "nodemon -r dotenv/config ./bin/www",
        "start:production": "node ./bin/www",
        "db:migrate": "dotenv sequelize-cli db:migrate",
        "db:migrate:undo:all": "dotenv sequelize-cli db:migrate:undo:all",  
        "db:redo": "npm run db:seed:undo:all && npm run db:migrate:undo:all && npm run db:migrate && npm run db:seed:all",
        "db:seed:all": "dotenv sequelize-cli db:seed:all",
        "db:seed:undo:all": "dotenv sequelize-cli db:seed:undo:all",
        "db:drop": "dotenv sequelize-cli db:drop",
        "db:create": "dotenv sequelize-cli db:create",
        "db:reset": "npm run db:drop && npm run db:create && npm run db:migrate && npm run db:seed:all",
        }



if __name__ == "__main__":
  
  if (len(sys.argv) < 3):
    sys.exit("Usage: gitProject.py <gitRepo> <folderName>")


  os.system(f'git clone {sys.argv[1]} ./{sys.argv[2]}')
  
  
  env_file = open(f'./{sys.argv[2]}/backend/.env', 'w+')
  env_file.writelines(env_params)
  env_file.close()
  
  with open(f'./{sys.argv[2]}/backend/package.json', 'r+') as f:
    data = json.load(f)
    data['scripts'] = package_params
    f.seek(0)
    json.dump(data, f, indent=2)
    f.truncate()
    
  
  
  os.system(f'rm -f ./{sys.argv[2]}/backend/package-lock.json')
  os.system(f'rm -f ./{sys.argv[2]}/frontend/package-lock.json')
  
  os.system(f'npm install --prefix ./{sys.argv[2]}/backend')
  os.system(f'npm run db:reset --prefix ./{sys.argv[2]}/backend')
  os.system(f'npm install --prefix ./{sys.argv[2]}/frontend')
  
  os.system(f'code {sys.argv[2]}')