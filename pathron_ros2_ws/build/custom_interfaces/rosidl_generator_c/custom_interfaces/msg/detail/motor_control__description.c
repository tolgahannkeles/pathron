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
      0x8a, 0x3b, 0x2b, 0x8f, 0xcf, 0xf0, 0xb1, 0x35,
      0x67, 0x85, 0x72, 0xf0, 0xe4, 0xc5, 0xd4, 0x93,
      0x79, 0xa9, 0x64, 0x08, 0xaf, 0xa6, 0x54, 0x82,
      0x83, 0x9d, 0x8c, 0x2a, 0x08, 0xef, 0x61, 0x85,
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
static char custom_interfaces__msg__MotorControl__FIELD_NAME__front_left[] = "front_left";
static char custom_interfaces__msg__MotorControl__FIELD_NAME__front_right[] = "front_right";
static char custom_interfaces__msg__MotorControl__FIELD_NAME__rear_left[] = "rear_left";
static char custom_interfaces__msg__MotorControl__FIELD_NAME__rear_right[] = "rear_right";

static rosidl_runtime_c__type_description__Field custom_interfaces__msg__MotorControl__FIELDS[] = {
  {
    {custom_interfaces__msg__MotorControl__FIELD_NAME__front_left, 10, 10},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_UINT8,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {custom_interfaces__msg__MotorControl__FIELD_NAME__front_right, 11, 11},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_UINT8,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {custom_interfaces__msg__MotorControl__FIELD_NAME__rear_left, 9, 9},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_UINT8,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {custom_interfaces__msg__MotorControl__FIELD_NAME__rear_right, 10, 10},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_UINT8,
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
      {custom_interfaces__msg__MotorControl__FIELDS, 4, 4},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "uint8 front_left\n"
  "uint8 front_right\n"
  "uint8 rear_left\n"
  "uint8 rear_right";

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
    {toplevel_type_raw_source, 67, 67},
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
