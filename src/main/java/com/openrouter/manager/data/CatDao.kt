import androidx.room.Dao
import androidx.room.Insert
import androidx.room.Query

@Dao
interface CatDao {
    @Insert
    suspend fun insertCat(cat: Cat)

    @Query("SELECT * FROM Cat")
    suspend fun getAllCats(): List<Cat>
}
