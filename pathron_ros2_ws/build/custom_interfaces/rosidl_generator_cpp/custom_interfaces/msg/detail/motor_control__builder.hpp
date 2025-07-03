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

class Init_MotorControl_rear_right
{
public:
  explicit Init_MotorControl_rear_right(::custom_interfaces::msg::MotorControl & msg)
  : msg_(msg)
  {}
  ::custom_interfaces::msg::MotorControl rear_right(::custom_interfaces::msg::MotorControl::_rear_right_type arg)
  {
    msg_.rear_right = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interfaces::msg::MotorControl msg_;
};

class Init_MotorControl_rear_left
{
public:
  explicit Init_MotorControl_rear_left(::custom_interfaces::msg::MotorControl & msg)
  : msg_(msg)
  {}
  Init_MotorControl_rear_right rear_left(::custom_interfaces::msg::MotorControl::_rear_left_type arg)
  {
    msg_.rear_left = std::move(arg);
    return Init_MotorControl_rear_right(msg_);
  }

private:
  ::custom_interfaces::msg::MotorControl msg_;
};

class Init_MotorControl_front_right
{
public:
  explicit Init_MotorControl_front_right(::custom_interfaces::msg::MotorControl & msg)
  : msg_(msg)
  {}
  Init_MotorControl_rear_left front_right(::custom_interfaces::msg::MotorControl::_front_right_type arg)
  {
    msg_.front_right = std::move(arg);
    return Init_MotorControl_rear_left(msg_);
  }

private:
  ::custom_interfaces::msg::MotorControl msg_;
};

class Init_MotorControl_front_left
{
public:
  Init_MotorControl_front_left()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MotorControl_front_right front_left(::custom_interfaces::msg::MotorControl::_front_left_type arg)
  {
    msg_.front_left = std::move(arg);
    return Init_MotorControl_front_right(msg_);
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
  return custom_interfaces::msg::builder::Init_MotorControl_front_left();
}

}  // namespace custom_interfaces

#endif  // CUSTOM_INTERFACES__MSG__DETAIL__MOTOR_CONTROL__BUILDER_HPP_
