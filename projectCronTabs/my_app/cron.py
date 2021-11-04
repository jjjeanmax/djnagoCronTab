from .models import Test, Document
from datetime import datetime as dt


def my_scheduled_job():
    Test.objects.create(name='test')


def document_expired_check():
    today = dt.today().strftime('%Y-%m-%d')
    document = Document.objects.filter(expired=False)
    for doc in document:
        expired_doc = doc.expiration_date.strftime('%Y-%m-%d')
        if expired_doc < today:
            doc.expired = True
            doc.save()
