class CreateUsers < ActiveRecord::Migration[5.2]
  def change
    create_table :users do |t|
      t.string :name, limit:191, null:false
      t.string :mail, limit:191, null:false
      t.string :password_digest, 191, null:false
      t.string :remember_token, 191

      t.datetime "created_at", null: false
      t.datetime "updated_at", null: false

      t.timestamps
    end
  end
end
