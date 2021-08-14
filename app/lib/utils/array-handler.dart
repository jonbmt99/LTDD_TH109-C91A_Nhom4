class ArrayHandler<T> {
  List<T> upsert(List<T> arr, T item) {
    final i = arr.indexWhere((_item) => (_item as dynamic)?.id == (item as dynamic)?.id);
    if (i > -1) {
      arr[i] = item;
    } else {
      arr.add(item);
    }
    return arr;
  }
}
