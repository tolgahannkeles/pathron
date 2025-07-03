// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from custom_interfaces:msg/MotorControl.idl
// generated code does not contain a copyright notice

#include "custom_interfaces/msg/detail/motor_control__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_custom_interfaces
const rosidl_type_hash_t *
custom_interfaces__msg__MotorControl__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x98, 0x7b, 0x1a, 0xb6, 0xa6, 0x21, 0xcf, 0xa7,
      0x4c, 0x61, 0x20, 0xf6, 0xe8, 0xef, 0xcb, 0x72,
      0x96, 0xa1, 0x56, 0x22, 0x65, 0xb7, 0x65, 0xb4,
      0x22, 0x63, 0x75, 0x54, 0xe7, 0x8b, 0xfe, 0xf1,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char custom_interfaces__msg__MotorControl__TYPE_NAME[] = "custom_interfaces/msg/MotorControl";

// Define type names, field names, and default values
static char custom_interfaces__msg__MotorControl__FIELD_NAME__linear_velocity[] = "linear_velocity";
static char custom_interfaces__msg__MotorControl__FIELD_NAME__angular_velocity[] = "angular_velocity";

static rosidl_runtime_c__type_description__Field custom_interfaces__msg__MotorControl__FIELDS[] = {
  {
    {custom_interfaces__msg__MotorControl__FIELD_NAME__linear_velocity, 15, 15},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT8,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {custom_interfaces__msg__MotorControl__FIELD_NAME__angular_velocity, 16, 16},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT8,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
custom_interfaces__msg__MotorControl__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {custom_interfaces__msg__MotorControl__TYPE_NAME, 34, 34},
      {custom_interfaces__msg__MotorControl__FIELDS, 2, 2},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "int8 linear_velocity   # -100: tam geri, 0: dur, +100: tam ileri\n"
  "int8 angular_velocity  # -100: sola tam d\\xc3\\xb6n, 0: d\\xc3\\xbcz, +100: sa\\xc4\\x9fa tam d\\xc3\\xb6n";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
custom_interfaces__msg__MotorControl__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {custom_interfaces__msg__MotorControl__TYPE_NAME, 34, 34},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 136, 136},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
custom_interfaces__msg__MotorControl__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *custom_interfaces__msg__MotorControl__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
