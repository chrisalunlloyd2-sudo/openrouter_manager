import androidx.room.Database
import androidx.room.Entity
import androidx.room.Room
import androidx.room.RoomDatabase

@Database(entities = [Cat::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun catDao(): CatDao
}

@Entity
data class Cat(
    @PrimaryKey val id: Int,
    val name: String,
    val age: Int
)
