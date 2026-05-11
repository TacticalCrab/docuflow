from .models import Document

def sidebar_documents(request):
    if request.user.is_authenticated:
        return {
            'sidebar_docs': Document.objects.filter(
                workspace__memberships__user=request.user
            ).distinct().order_by('-updated_at')[:10]
        }
    return {}