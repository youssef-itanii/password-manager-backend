CREATE OR ALTER PROCEDURE [dbo].[Profile_Verify]
(
	@Profile_id INT
	,@Verification_Code VARCHAR(6)
)
AS
SET NOCOUNT ON;
IF EXISTS (SELECT * FROM Verification_Code WHERE @Profile_id = profile_id AND @Verification_Code=code_value)
	BEGIN
		INSERT INTO Verfied_Profile (profile_id) VALUES (@Profile_id)
	SELECT 'You have been verified' [message] FOR JSON PATH;
	END
ELSE
	SELECT 'Invalid verficiation code' [message] FOR JSON PATH;
GO
