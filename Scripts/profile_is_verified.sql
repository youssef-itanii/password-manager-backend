CREATE OR ALTER PROCEDURE [dbo].[profile_is_verified](
	@Profile_id INT
)
AS
IF EXISTS (SELECT * FROM [dbo].[Verfied_Profile])
	BEGIN
		SELECT 1 [verified] FOR JSON PATH;
	END
ELSE 
	SELECT 0 [verified] FOR JSON PATH;

GO