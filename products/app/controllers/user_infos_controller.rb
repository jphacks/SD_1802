class UserInfosController < ApplicationController
  def new
    @info = UserInfo.find_by(user_id: @current_user.id)
    if @info.present?
      redirect_to profile_show_path
    else
      @info = UserInfo.new(user_id: @current_user.id)
    end
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
