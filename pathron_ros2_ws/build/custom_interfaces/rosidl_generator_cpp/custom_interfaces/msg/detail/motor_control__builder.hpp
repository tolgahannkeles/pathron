// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_interfaces:msg/MotorControl.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "custom_interfaces/msg/motor_control.hpp"


#ifndef CUSTOM_INTERFACES__MSG__DETAIL__MOTOR_CONTROL__BUILDER_HPP_
#define CUSTOM_INTERFACES__MSG__DETAIL__MOTOR_CONTROL__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "custom_interfaces/msg/detail/motor_control__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace custom_interfaces
{

namespace msg
{

namespace builder
{

class Init_MotorControl_angular_velocity
{
public:
  explicit Init_MotorControl_angular_velocity(::custom_interfaces::msg::MotorControl & msg)
  : msg_(msg)
  {}
  ::custom_interfaces::msg::MotorControl angular_velocity(::custom_interfaces::msg::MotorControl::_angular_velocity_type arg)
  {
    msg_.angular_velocity = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interfaces::msg::MotorControl msg_;
};

class Init_MotorControl_linear_velocity
{
public:
  Init_MotorControl_linear_velocity()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MotorControl_angular_velocity linear_velocity(::custom_interfaces::msg::MotorControl::_linear_velocity_type arg)
  {
    msg_.linear_velocity = std::move(arg);
    return Init_MotorControl_angular_velocity(msg_);
  }

private:
  ::custom_interfaces::msg::MotorControl msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interfaces::msg::MotorControl>()
{
  return custom_interfaces::msg::builder::Init_MotorControl_linear_velocity();
}

}  // namespace custom_interfaces

#endif  // CUSTOM_INTERFACES__MSG__DETAIL__MOTOR_CONTROL__BUILDER_HPP_
