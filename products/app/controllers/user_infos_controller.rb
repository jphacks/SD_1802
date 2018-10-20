class UserInfosController < ApplicationController
  def new
    @info = UserInfo.new(user_id: @current_user.id)
  end

  def show
    @infos = UserInfo.all
  end

  def create
    @info = UserInfo.new(params.require(:user_info).permit(:name, :file, :user_id, :memo))
    @info.save
    redirect_to profile_show_path
  end

end
