from django.shortcuts import redirect

class AdminAccessMixin:
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('accounts:login')
    
    
class AdminStaffAccessMixin:
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated  or request.user.is_staff:
            return super().dispatch(request, *args, **kwargs)
        return redirect('accounts:login')


class AdminAgentMixin:
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated  or self.get_object().agent == request.user:
            return super().dispatch(request, *args, **kwargs)
        return redirect('accounts:login')

class AgentMixin:
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object().agent == request.user:
            return super().dispatch(request, *args, **kwargs)
        return redirect('accounts:profile')


class InquiryPropertyAgentMixin:
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object().property.agent == request.user:
            return super().dispatch(request, *args, **kwargs)
        return redirect('inquiry:inquiry_list')