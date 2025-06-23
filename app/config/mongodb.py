from datetime import timedelta
import os
from dotenv import load_dotenv
from pymongo import ASCENDING, IndexModel, DESCENDING
from pymongo.errors import OperationFailure

# Load environment variables
load_dotenv()

class MongoConfig:
    # MongoDB Settings
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/exampro')
    
    # Collection Names
    USERS_COLLECTION = 'users'
    EXAMS_COLLECTION = 'exams'
    SUBMISSIONS_COLLECTION = 'submissions'
    CLASSES_COLLECTION = 'classes'
    
    # Indexes
    INDEXES = {
        USERS_COLLECTION: [
            IndexModel([('email', ASCENDING)], unique=True),
            IndexModel([('username', ASCENDING)], unique=True),
            IndexModel([('student_id', ASCENDING)], unique=True, sparse=True),
            IndexModel([('role', ASCENDING)]),
            IndexModel([('created_at', DESCENDING)])
        ],
        EXAMS_COLLECTION: [
            IndexModel([('teacher_id', ASCENDING)]),
            IndexModel([('start_time', ASCENDING)]),
            IndexModel([('end_time', ASCENDING)]),
            IndexModel([('is_active', ASCENDING)])
        ],
        SUBMISSIONS_COLLECTION: [
            IndexModel([('exam_id', ASCENDING)]),
            IndexModel([('student_id', ASCENDING)]),
            IndexModel([('submitted_at', DESCENDING)]),
            IndexModel([('is_graded', ASCENDING)])
        ],
        CLASSES_COLLECTION: [
            IndexModel([('teacher_id', ASCENDING)]),
            IndexModel([('students', ASCENDING)]),
            IndexModel([('created_at', DESCENDING)])
        ]
    }
    
    # Default Values
    DEFAULT_PAGE_SIZE = 10
    MAX_PAGE_SIZE = 100
    
    # Timeouts
    MONGO_CONNECT_TIMEOUT_MS = 5000
    MONGO_SOCKET_TIMEOUT_MS = 10000
    
    # Cache Settings
    CACHE_TIMEOUT = timedelta(minutes=5)
    
    @classmethod
    def init_indexes(cls, mongo):
        """Initialize all MongoDB indexes"""
        try:
            for collection_name, indexes in cls.INDEXES.items():
                collection = mongo.db[collection_name]
                existing_indexes = collection.list_indexes()
                existing_index_names = [idx['name'] for idx in existing_indexes]
                
                for index in indexes:
                    if index.document.get('name') not in existing_index_names:
                        try:
                            collection.create_indexes([index])
                            print(f"Created index {index.document.get('name')} on {collection_name}")
                        except OperationFailure as e:
                            print(f"Error creating index on {collection_name}: {str(e)}")
            
            print("MongoDB indexes initialized successfully")
            return True
        except Exception as e:
            print(f"Error initializing MongoDB indexes: {str(e)}")
            return False

    @staticmethod
    def init_collections(mongo):
        try:
            # Create collections if they don't exist
            collections = mongo.db.list_collection_names()
            
            if 'users' not in collections:
                mongo.db.create_collection('users')
            
            if 'exams' not in collections:
                mongo.db.create_collection('exams')
            
            if 'submissions' not in collections:
                mongo.db.create_collection('submissions')

            print("MongoDB collections initialized successfully")
            
        except Exception as e:
            print(f"Error creating collections: {str(e)}")
            raise 