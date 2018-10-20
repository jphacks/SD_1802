require 'test_helper'

class UserInfosControllerTest < ActionDispatch::IntegrationTest
  test "should get new" do
    get user_infos_new_url
    assert_response :success
  end

  test "should get show" do
    get user_infos_show_url
    assert_response :success
  end

  test "should get upload" do
    get user_infos_upload_url
    assert_response :success
  end

  test "should get create" do
    get user_infos_create_url
    assert_response :success
  end

end
