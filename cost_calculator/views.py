from django.shortcuts import render, redirect
from django.http import HttpResponseServerError
from django.views import View

from .models import Item


class AddItemsView(View):
    def get(self, request):
        return render(request, 'add_items.html')


class SaveItemsView(View):
    def post(self, request):
        try:
            price_list = request.POST.getlist('price[]')
            item_list = request.POST.getlist('item[]')

            recently_added_items = []  # Initialize a list to store recently added items

            # Save items and prices to the database
            for price, item in zip(price_list, item_list):
                if price.strip() and item.strip():  # Check if both price and item are not empty
                    new_item = Item.objects.create(price=price, name=item)
                    recently_added_items.append(new_item)  # Append the newly created item to the list

            # Store the recently added items in the session
            request.session['recent_items'] = [item.id for item in recently_added_items]

            return redirect('summary')

        except Exception as e:
            print(f"Error occurred: {e}")
            return HttpResponseServerError("An error occurred while saving items. Please try again later.")


class SummaryView(View):
    def get(self, request):
        try:
            recent_item_ids = request.session.get('recent_items', [])
            recent_items = Item.objects.filter(id__in=recent_item_ids)

            total_price = sum(item.price for item in recent_items)

            return render(request, 'summary.html', {'recent_items': recent_items, 'total_price': total_price})

        except Exception as e:
            print(f"Error occurred: {e}")
            return HttpResponseServerError("An error occurred while generating the summary.")


class ShowAddItemsView(View):
    def get(self, request):
        return render(request, 'add_items.html')
