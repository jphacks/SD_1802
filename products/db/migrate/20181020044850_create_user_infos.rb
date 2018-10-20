class CreateUserInfos < ActiveRecord::Migration[5.2]
  def change
    create_table :user_infos do |t|
      t.string :name
      t.string :file
      t.string :memo
      t.references :user, foreign_key: true

      t.timestamps
    end
  end
end
