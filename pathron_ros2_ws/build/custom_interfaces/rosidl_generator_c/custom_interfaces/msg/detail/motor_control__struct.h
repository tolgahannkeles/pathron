// NOLINT: This file starts with a BOM since it contain non-ASCII characters
// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from custom_interfaces:msg/MotorControl.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "custom_interfaces/msg/motor_control.h"


#ifndef CUSTOM_INTERFACES__MSG__DETAIL__MOTOR_CONTROL__STRUCT_H_
#define CUSTOM_INTERFACES__MSG__DETAIL__MOTOR_CONTROL__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

/// Struct defined in msg/MotorControl in the package custom_interfaces.
typedef struct custom_interfaces__msg__MotorControl
{
  /// -100: tam geri, 0: dur, +100: tam ileri
  int8_t linear_velocity;
  /// -100: sola tam dön, 0: düz, +100: sağa tam dön
  int8_t angular_velocity;
} custom_interfaces__msg__MotorControl;

// Struct for a sequence of custom_interfaces__msg__MotorControl.
typedef struct custom_interfaces__msg__MotorControl__Sequence
{
  custom_interfaces__msg__MotorControl * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} custom_interfaces__msg__MotorControl__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CUSTOM_INTERFACES__MSG__DETAIL__MOTOR_CONTROL__STRUCT_H_
