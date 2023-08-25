def rename_column(obj):
    obj.rename(columns = { "Life expectancy at birth (years)" : "LEABY" }, inplace = True)
    obj.head()