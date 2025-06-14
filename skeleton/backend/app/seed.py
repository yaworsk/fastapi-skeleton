"""
Seed script for populating the database with sample data.
Run with: make seed
"""

from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.user import User
from app.models.item import Item

def seed_database():
    """Seed the database with sample data."""
    db: Session = SessionLocal()
    
    try:
        # Check if data already exists
        if db.query(User).first():
            print("Database already contains data. Skipping seed.")
            return
        
        # Create sample users
        users = [
            User(
                email="john.doe@example.com",
                first_name="John",
                last_name="Doe",
                is_active=True
            ),
            User(
                email="jane.smith@example.com",
                first_name="Jane",
                last_name="Smith",
                is_active=True
            ),
            User(
                email="bob.wilson@example.com",
                first_name="Bob",
                last_name="Wilson",
                is_active=False
            )
        ]
        
        for user in users:
            db.add(user)
        
        # Create sample items
        items = [
            Item(
                title="Sample Item 1",
                description="This is a sample item for testing purposes.",
                is_active=True
            ),
            Item(
                title="Sample Item 2",
                description="Another sample item with different content.",
                is_active=True
            ),
            Item(
                title="Inactive Item",
                description="This item is marked as inactive.",
                is_active=False
            )
        ]
        
        for item in items:
            db.add(item)
        
        db.commit()
        print("✅ Database seeded successfully!")
        print(f"Created {len(users)} users and {len(items)} items.")
        
    except Exception as e:
        print(f"❌ Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()
