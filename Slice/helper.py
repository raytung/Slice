from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def get_sorted_model(request, model):
    sort = request.GET.get('sort', None)
    obj = model

    if sort == "price_lth":
        obj = model.order_by('cost_per_unit')
    elif sort == "price_htl":
        obj = model.order_by('-cost_per_unit')
    elif sort == "end_lth":
        obj = model.order_by('end_date')
    elif sort =="end_htl":
        obj = model.order_by('-end_date')
    elif sort == "alpha_lth":
        obj = model.order_by('title')
    elif sort == "alpha_htl":
        obj = model.order_by('-title')
    elif sort == "end_date_lth":
        obj = model.order_by('end_date')
    elif sort == "end_date_htl":
        obj = model.order_by('-end_date')
    elif sort == "start_date_lth":
        obj = model.order_by('start_date')
    elif sort == "start_date_htl":
        obj = model.order_by('-start_date')

    return obj

def get_paginator(obj, request, per_page=5):
  paginator  = Paginator(obj, per_page)
  page = request.GET.get('page')
  try:
      temp = paginator.page(page)
  except PageNotAnInteger:
      temp = paginator.page(1)
  except EmptyPage:
      temp = paginator.page(paginator.num_pages)
  return temp, paginator.num_pages
