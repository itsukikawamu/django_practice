class DatabaseRouter:
    app_labels = {
        "youtube": "youtube_db"
    }
    
    def db_for_read(self, model, **hints):
        return self.app_labels.get(model._meta.app_label, "default")
    
    def db_for_write(self, model, **hints):
        return self.app_labels.get(model._meta.app_label, "default")
    
    def allow_relation(self, obj1, obj2, **hints):
        if obj1._state.db == obj2._state.db:
            return True
        return None
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.app_labels:
            return db == self.app_labels[app_label]
        return db == "default"