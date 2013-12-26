/* Software License Agreement (BSD License)
 *
 * Copyright (c) 2011, Willow Garage, Inc.
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 *  * Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 *  * Redistributions in binary form must reproduce the above
 *    copyright notice, this list of conditions and the following
 *    disclaimer in the documentation and/or other materials provided
 *    with the distribution.
 *  * Neither the name of Willow Garage, Inc. nor the names of its
 *    contributors may be used to endorse or promote products derived
 *    from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 * FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 * INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 * BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 * CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 * ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 *
 * Auto-generated by gensrv_cpp from file /svn/svn_components/robotnik_msgs/groovy/robotnik_msgs/srv/set_height.srv
 *
 */


#ifndef ROBOTNIK_MSGS_MESSAGE_SET_HEIGHT_H
#define ROBOTNIK_MSGS_MESSAGE_SET_HEIGHT_H

#include <ros/service_traits.h>


#include <robotnik_msgs/set_heightRequest.h>
#include <robotnik_msgs/set_heightResponse.h>


namespace robotnik_msgs
{

struct set_height
{

typedef set_heightRequest Request;
typedef set_heightResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct set_height
} // namespace robotnik_msgs


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::robotnik_msgs::set_height > {
  static const char* value()
  {
    return "30c54779fb893ca6d32239f321774b5f";
  }

  static const char* value(const ::robotnik_msgs::set_height&) { return value(); }
};

template<>
struct DataType< ::robotnik_msgs::set_height > {
  static const char* value()
  {
    return "robotnik_msgs/set_height";
  }

  static const char* value(const ::robotnik_msgs::set_height&) { return value(); }
};


// service_traits::MD5Sum< ::robotnik_msgs::set_heightRequest> should match 
// service_traits::MD5Sum< ::robotnik_msgs::set_height > 
template<>
struct MD5Sum< ::robotnik_msgs::set_heightRequest>
{
  static const char* value()
  {
    return MD5Sum< ::robotnik_msgs::set_height >::value();
  }
  static const char* value(const ::robotnik_msgs::set_heightRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::robotnik_msgs::set_heightRequest> should match 
// service_traits::DataType< ::robotnik_msgs::set_height > 
template<>
struct DataType< ::robotnik_msgs::set_heightRequest>
{
  static const char* value()
  {
    return DataType< ::robotnik_msgs::set_height >::value();
  }
  static const char* value(const ::robotnik_msgs::set_heightRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::robotnik_msgs::set_heightResponse> should match 
// service_traits::MD5Sum< ::robotnik_msgs::set_height > 
template<>
struct MD5Sum< ::robotnik_msgs::set_heightResponse>
{
  static const char* value()
  {
    return MD5Sum< ::robotnik_msgs::set_height >::value();
  }
  static const char* value(const ::robotnik_msgs::set_heightResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::robotnik_msgs::set_heightResponse> should match 
// service_traits::DataType< ::robotnik_msgs::set_height > 
template<>
struct DataType< ::robotnik_msgs::set_heightResponse>
{
  static const char* value()
  {
    return DataType< ::robotnik_msgs::set_height >::value();
  }
  static const char* value(const ::robotnik_msgs::set_heightResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // ROBOTNIK_MSGS_MESSAGE_SET_HEIGHT_H