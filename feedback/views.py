from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from .models import Item, Feedback
from .forms import FeedbackForm

def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)  
    feedback_list = Feedback.objects.filter(item=item)
    average_rating = feedback_list.aggregate(Avg('rating'))['rating__avg'] or 0

    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.item = item 
            feedback.save()
            return redirect('item_detail', item_id=item.id)  
    else:
        form = FeedbackForm()

    context = {
        'item': item,
        'feedback_list': feedback_list,
        'average_rating': average_rating,
        'form': form,
    }
    return render(request, 'feedback/item_detail.html', context)
