from .models import Document

def sidebar_documents(request):
    if request.user.is_authenticated:
        # This makes 'sidebar_docs' available in EVERY template
        return {
            'sidebar_docs': Document.objects.filter(owner=request.user).order_by('-updated_at')[:10]
        }
    return {}