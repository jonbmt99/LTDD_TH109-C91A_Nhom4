import 'package:json_annotation/json_annotation.dart';

part 'Category.g.dart';

@JsonSerializable()
class Category {
  @JsonKey(name: 'category_id')
  int id;

  @JsonKey(name: 'category_name')
  String fullName;

  @JsonKey(name: 'image')
  String image;

  Category({
    this.id,
    this.fullName,
    this.image,
  });

  factory Category.fromJson(Map<String, dynamic> json) => _$CategoryFromJson(json);

  Map<String, dynamic> toJson() => _$CategoryToJson(this);
}
