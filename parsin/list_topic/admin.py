from django.contrib import admin 
from .models import Post

@admin.register(Post) 
class PostAdmin(admin.ModelAdmin):    
    list_display = ('Research_title', 'slug', 'author', 'publish','visits', 'status')    
    list_filter = ('status', 'created', 'publish', 'author')    
    search_fields = ('Research_title', 'Research_content')    
    prepopulated_fields = {'slug': ('Research_title',)}    
    raw_id_fields = ('author',)    
    date_hierarchy = 'publish'    
    ordering = ('status', '-publish')  