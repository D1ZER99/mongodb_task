# MongoDB Docker Setup

This project provides a quick setup for running MongoDB in Docker with shell access for running commands.

## Prerequisites

- Docker Desktop installed and running
- Docker Compose installed (comes with Docker Desktop on Windows)

## Quick Start

### 1. Start MongoDB Container

```bash
docker-compose up -d
```

This will:
- Pull the latest MongoDB image
- Start MongoDB on port 27017
- Create persistent volumes for data
- Set up admin credentials (username: admin, password: password123)

### 2. Access MongoDB Shell

#### Option 1: Using docker exec (Recommended)
```bash
docker exec -it mongodb_local mongosh -u admin -p password123 --authenticationDatabase admin
```

#### Option 2: Without authentication (for testing)
```bash
docker exec -it mongodb_local mongosh
```

### 3. Stop MongoDB Container

```bash
docker-compose down
```

To stop and remove volumes (delete all data):
```bash
docker-compose down -v
```

## MongoDB Shell Commands

Once you're in the MongoDB shell, you can run these commands:

### Show Databases
```javascript
show dbs
```

### Create/Switch to Database
```javascript
use mydb
```

### Insert Data
```javascript
// Insert a single document
db.users.insertOne({
  name: "John Doe",
  email: "john@example.com",
  age: 30
})

// Insert multiple documents
db.users.insertMany([
  { name: "Jane Smith", email: "jane@example.com", age: 25 },
  { name: "Bob Johnson", email: "bob@example.com", age: 35 }
])
```

### Read/Query Data
```javascript
// Find all documents
db.users.find()

// Find with pretty formatting
db.users.find().pretty()

// Find with filter
db.users.find({ age: { $gte: 30 } })

// Find one document
db.users.findOne({ name: "John Doe" })
```

### Update Data
```javascript
// Update one document
db.users.updateOne(
  { name: "John Doe" },
  { $set: { age: 31 } }
)

// Update multiple documents
db.users.updateMany(
  { age: { $lt: 30 } },
  { $set: { status: "young" } }
)
```

### Delete Data
```javascript
// Delete one document
db.users.deleteOne({ name: "John Doe" })

// Delete multiple documents
db.users.deleteMany({ age: { $lt: 25 } })
```

### Show Collections
```javascript
show collections
```

### Count Documents
```javascript
db.users.countDocuments()
```

### Drop Collection
```javascript
db.users.drop()
```

## Connection String

To connect from applications:
```
mongodb://admin:password123@localhost:27017/mydb?authSource=admin
```

## Troubleshooting

### Check if container is running
```bash
docker ps
```

### View container logs
```bash
docker logs mongodb_local
```

### Restart container
```bash
docker-compose restart
```

### Access container bash
```bash
docker exec -it mongodb_local bash
```

## Default Credentials

- **Username:** admin
- **Password:** password123
- **Default Database:** mydb
- **Port:** 27017

**Note:** Change these credentials in production!
